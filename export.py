c = get_config()
c.NbConvertApp.notebooks = ["*.ipynb"]
c.NbConvertApp.export_format = "html"
c.FilesWriter.build_directory = "docs"
