from pathlib import Path


class Site:
    """Set configuration values and create root structure of static site
        Args:
            source: the source path, provides structure to be duplicated
            dest: the destination path, where structure is duplicated
        Returns:

    """

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = "/".join([self.dest, path.relative_to(self.source)])
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
