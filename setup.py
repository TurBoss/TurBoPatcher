import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
	base = 'Win32GUI'
	
executables = [
	Executable("App1.py",
				icon="tp.ico",
				base = base,
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
