from fields.core.spkg.builder import SpkgPackageBuilder
from fields.core.spkg.deb import SpkgDebPkgFormat


class SpkgBuild:
    def __init__(self, data: dict):
        self.compose_data = data

        self.meta = _SpkgPackageMeta()
        self.prepare = _SpkgPackagePrepare()
        self.build = _SpkgPackageBuild()
        self.install = _SpkgPackageInstall()

        self.builder = None
        self.install_pkg = None

        match data["Build"]["BuildSys"]:
            case "cargo":
                self.builder = SpkgPackageBuilder.Cargo(data)

        match data["Install"]["As"]:
            case "deb":
                self.install_pkg = SpkgDebPkgFormat(data)

        self.parse()

    def parse(self):
        self.meta.name = self.compose_data["Meta"]["Name"]
        self.meta.id = self.compose_data["Meta"]["Id"]
        self.meta.description = self.compose_data["Meta"]["Description"]
        self.meta.version = self.compose_data["Meta"]["Version"]
        self.meta.architecture = self.compose_data["Meta"]["Architecture"]
        self.meta.author = self.compose_data["Meta"]["Author"]

        self.prepare.type = self.compose_data["Prepare"]["Type"]
        self.prepare.url = self.compose_data["Prepare"]["URL"]

        self.build.build_system = self.compose_data["Build"]["BuildSys"]
        self.build.workdir = self.compose_data["Build"]["Workdir"]

        self.install.type_as = self.compose_data["Install"]["As"]


class _SpkgPackageMeta:
    def __init__(self):
        self.name = None
        self.id = None
        self.description = None
        self.version = None
        self.architecture = None
        self.author = None


class _SpkgPackagePrepare:
    def __init__(self):
        self.type = None
        self.url = None


class _SpkgPackageBuild:
    def __init__(self):
        self.build_system = None
        self.workdir = None


class _SpkgPackageInstall:
    def __init__(self):
        self.type_as = None

