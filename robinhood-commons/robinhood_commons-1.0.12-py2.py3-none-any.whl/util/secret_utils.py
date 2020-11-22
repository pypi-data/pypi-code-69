from __future__ import annotations

import base64
from typing import Dict

from botocore.exceptions import ClientError

from util.aws_utils import AwsUtils
from util.constants import USERS_KEY


class SecretUtils:

    @classmethod
    def get_secret(cls, secret_name: str, client=AwsUtils.create_boto_client()) -> Dict[str, str]:

        try:
            get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'DecryptionFailureException':
                # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
                raise e
            elif error_code == 'InternalServiceErrorException':
                # An error occurred on the server side.
                raise e
            elif error_code == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                raise e
            elif error_code == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                raise e
            elif error_code == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                raise e
            else:
                print(f'UNKNOWN error: {e}')
                raise e
        else:
            secret = get_secret_value_response['SecretString'] if 'SecretString' in get_secret_value_response else \
                base64.b64decode(get_secret_value_response['SecretBinary'])

            return eval(secret)


if __name__ == '__main__':
    print(SecretUtils.get_secret(client=AwsUtils.create_boto_client(), secret_name=USERS_KEY))
