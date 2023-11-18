from sqlalchemy.orm import registry


def mapper_registry_configure():
    mapper_registry = registry()
    mapper_registry.configure()
