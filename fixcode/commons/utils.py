from uuid import UUID

def is_valid_and_return_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return UUID(uuid_to_test, version=version)