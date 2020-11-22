from typing import List, Union

from pyspark.sql import Column, DataFrame
from pyspark.sql.functions import concat

from spark_auto_mapper.data_types.data_type_base import AutoMapperDataTypeBase
from spark_auto_mapper.data_types.text_like_base import AutoMapperTextLikeBase
from spark_auto_mapper.helpers.value_parser import AutoMapperValueParser
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeTextType
from spark_auto_mapper.type_definitions.wrapper_types import AutoMapperWrapperType


class AutoMapperConcatDataType(AutoMapperTextLikeBase):
    """
    Concatenates multiple strings together
    """
    def __init__(
        self, *args: Union[AutoMapperNativeTextType, AutoMapperWrapperType,
                           AutoMapperTextLikeBase]
    ):
        super().__init__()

        self.value: List[AutoMapperDataTypeBase] = [
            value if isinstance(value, AutoMapperDataTypeBase) else
            AutoMapperValueParser.parse_value(value) for value in args
        ]

    def get_column_spec(self, source_df: DataFrame) -> Column:
        column_spec = concat(
            *[col.get_column_spec(source_df=source_df) for col in self.value]
        )
        return column_spec
