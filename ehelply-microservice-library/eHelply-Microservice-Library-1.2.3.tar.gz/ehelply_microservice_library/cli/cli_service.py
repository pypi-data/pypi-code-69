import typer

cli = typer.Typer()


@cli.command()
def install():
    print("Not implemented")


@cli.command()
def seed():
    print("Not implemented")


@cli.command()
def export_docs():
    """Script to export the ReDoc documentation page into a standalone HTML file."""

    with typer.progressbar(length=8, label="Exporting") as progress:

        typer.echo("Starting doc exports. Expect to see lots of bootstrap text in the log")

        import json

        import sys

        from pathlib import Path

        from datetime import datetime

        from ehelply_microservice_library.cli.cli_state import CLIState

        class DocsService(CLIState.service):
            def if_dev_launch_dev_server(self) -> bool:
                return False

        progress.update(1)

        service = DocsService()

        progress.update(3)

        if service.fastapi_driver:
            app = service.fastapi_driver.instance

            HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>{service_name} {service_version} - Docs</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="{ehelply_logo_url}">
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
    </style>
    <style data-styled="" data-styled-version="4.4.1"></style>
</head>
<body>

    <div style='padding:25px;'>

        <h3>eHelply Microservice Documentation</h3>
        <a href="https://github.com/eHelply/docs-ehelply-microservices">Documentation Repository</a>

        <h4>{service_name} - {service_version}</h4>
        <a href="https://github.com/eHelply/docs-ehelply-microservices/{service_key}">{service_name} Documentation Revisions</a>

    </div>

    <hr>

    <div id="redoc-container"></div>
    <script src="https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"> </script>
    <script>
        var spec = %s;
        Redoc.init(spec, {{}}, document.getElementById("redoc-container"));
    </script>
</body>
</html>
            """.format(
                service_name=service.service_meta.name,
                service_key=service.service_meta.key,
                service_version=service.service_meta.version,
                ehelply_logo_url="https://assets.ehelply.com/logo/ehelply/base/symbol_transparent_white.png",
            )

            docs_file: str = datetime.utcnow().strftime(
                "api_docs." + service.service_meta.version + ".%Y%m%d-%H%M%S-utc.html")

            docs_location = Path(service.get_service_package_path()).resolve().joinpath('docs')
            docs_location.mkdir(exist_ok=True)

            progress.update(1)

            with open(docs_location.joinpath(docs_file), "w") as fd:
                print(HTML_TEMPLATE % json.dumps(app.openapi()), file=fd)

            progress.update(3)

        typer.echo("Doc export complete. Please check the docs folder.")

        sys.exit()


@cli.command()
def export_spec():
    """Script to export the ReDoc documentation page into a standalone HTML file."""

    with typer.progressbar(length=8, label="Exporting") as progress:
        typer.echo("Starting spec export. Expect to see lots of bootstrap text in the log")

        import json

        import sys

        from pathlib import Path

        from datetime import datetime

        from ehelply_microservice_library.cli.cli_state import CLIState

        class DocsService(CLIState.service):
            def if_dev_launch_dev_server(self) -> bool:
                return False

        progress.update(1)

        service = DocsService()

        progress.update(2)

        if service.fastapi_driver:
            app = service.fastapi_driver.instance

            docs_file: str = datetime.utcnow().strftime(
                "api_spec." + service.service_meta.version + ".%Y%m%d-%H%M%S-utc.json")

            docs_location = Path(service.get_service_package_path()).resolve().joinpath('docs')
            docs_location.mkdir(exist_ok=True)

            progress.update(1)

            data: dict = {
                "meta": service.service_meta.dict(),
                "spec": app.openapi()
            }

            progress.update(3)

            with open(docs_location.joinpath(docs_file), "w") as fd:
                json.dump(data, fd)

            progress.update(1)

        typer.echo("Doc export complete. Please check the docs folder.")

        sys.exit()


if __name__ == '__main__':
    cli()
