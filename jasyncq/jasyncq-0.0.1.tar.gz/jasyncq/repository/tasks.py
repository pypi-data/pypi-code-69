import json
import logging
import time
import uuid
from typing import List, Any

from aiomysql import Pool
from pypika import Query, Table

from jasyncq.model.task import TaskStatus
from jasyncq.repository.abstract import AbstractRepository


class TaskRepository(AbstractRepository):
    def __init__(self, pool: Pool):
        super().__init__(pool=pool)
        self.table_name = 'task'
        self.task = Table(self.table_name)
        self.task__uuid = self.task.field('uuid')
        self.task__status = self.task.field('status')
        self.task__progressed_at = self.task.field('progressed_at')
        self.task__scheduled_at = self.task.field('scheduled_at')
        self.task__is_urgent = self.task.field('is_urgent')
        self.task__task = self.task.field('task')

    def with_locked_table(self, query: List[str]) -> List[str]:
        return [
            f'LOCK TABLES {self.table_name} WRITE',
            *query,
            'UNLOCK TABLES'
        ]

    async def fetch_scheduled_tasks(
        self,
        offset: int,
        limit: int
    ) -> List[Any]:
        current_epoch = time.time()
        fetch_filter = (self.task__status == int(TaskStatus.QUEUED)) & (
            (self.task__scheduled_at <= current_epoch))
        get_tasks_query = Query.from_(self.task).select(
            self.task__uuid,
            self.task__status,
            self.task__progressed_at,
            self.task__scheduled_at,
            self.task__is_urgent,
            self.task__task,
        ).where(fetch_filter).offset(offset).limit(limit).get_sql(quote_char='`')
        logging.debug(get_tasks_query)

        update_tasks_status = Query.update(self.task).set(
            self.task__status, int(TaskStatus.WORK_IN_PROGRESS)
        ).set(
            self.task__progressed_at, int(current_epoch)
        ).where(fetch_filter).offset(offset).limit(limit).get_sql(quote_char='`')
        logging.debug(update_tasks_status)

        task_rows = (await self._execute_and_fetch(self.with_locked_table([
            get_tasks_query,
            update_tasks_status,
        ])))[1]
        logging.debug(task_rows)
        return task_rows

    async def fetch_pending_tasks(
        self,
        offset: int,
        limit: int,
        check_term_seconds: int = 30
    ) -> List[Any]:
        current_epoch = time.time()
        fetch_filter = (self.task__status == int(TaskStatus.WORK_IN_PROGRESS)) & (
            self.task__progressed_at <= (int(current_epoch) - check_term_seconds))
        get_tasks_query = Query.from_(self.task).select(
            self.task__uuid,
            self.task__status,
            self.task__progressed_at,
            self.task__scheduled_at,
            self.task__is_urgent,
            self.task__task,
        ).where(fetch_filter).offset(offset).limit(limit).get_sql(quote_char='`')
        logging.debug(get_tasks_query)

        update_tasks_status = Query.update(self.task).set(
            self.task__status, int(TaskStatus.WORK_IN_PROGRESS)
        ).set(
            self.task__progressed_at, int(current_epoch)
        ).where(fetch_filter).offset(offset).limit(limit).get_sql(quote_char='`')
        logging.debug(update_tasks_status)

        task_rows = (await self._execute_and_fetch(self.with_locked_table([
            get_tasks_query,
            update_tasks_status,
        ])))[1]
        logging.debug(task_rows)
        return task_rows

    async def insert_tasks(self, tasks: List[dict], scheduled_at: int=0):
        logging.debug(tasks)
        insert_tasks_query = Query.into(self.task)
        for task in tasks:
            insert_tasks_query = insert_tasks_query.insert(
                str(uuid.uuid4()),
                int(TaskStatus.QUEUED),
                0,
                scheduled_at,
                False,
                json.dumps(task)
            )
        insert_tasks_query = insert_tasks_query.get_sql(quote_char='`')
        logging.debug(insert_tasks_query)
        await self._execute([insert_tasks_query])

    async def delete_tasks(self, task_ids: List[str]):
        logging.debug(task_ids)
        fetch_filter = self.task__uuid.isin(task_ids)
        delete_tasks_query = Query.from_(self.task).where(
            fetch_filter
        ).delete().get_sql(quote_char='`')
        logging.debug(delete_tasks_query)
        await self._execute([delete_tasks_query])
