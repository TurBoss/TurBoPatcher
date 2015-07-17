from cx_Freeze import setup, Executable


executables = [
    Executable("App1.py",
               #icon="logo.ico",
               base = "Win32GUI",
               appendScriptToExe=True,
               appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False,)
setup(name="FF7 patcher",
      version="0.1",
      description="Create Patchs and patch files",
      options=dict(build_exe=buildOptions),
      executables=executables,
      )
