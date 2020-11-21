from typing import List, Union, TypeVar

from pyspark.sql import Column, DataFrame
from pyspark.sql.functions import coalesce

from spark_auto_mapper.data_types.data_type_base import AutoMapperDataTypeBase
from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase
from spark_auto_mapper.helpers.value_parser import AutoMapperValueParser
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

_T = TypeVar(
    "_T", bound=Union[AutoMapperNativeSimpleType, AutoMapperDataTypeBase]
)


class AutoMapperCoalesceDataType(AutoMapperTextLikeBase):
    """
    Returns the first column that is not null.
    """
    def __init__(
        self,
        *args: _T,
    ):
        super().__init__()

        self.value: List[AutoMapperDataTypeBase] = [
            value if isinstance(value, AutoMapperDataTypeBase) else
            AutoMapperValueParser.parse_value(value) for value in args
        ]

    def get_column_spec(self, source_df: DataFrame) -> Column:
        column_spec = coalesce(
            *[col.get_column_spec(source_df=source_df) for col in self.value]
        )
        return column_spec

    def include_null_properties(self, include_null_properties: bool) -> None:
        for item in self.value:
            item.include_null_properties(
                include_null_properties=include_null_properties
            )
