# Example of "R.Net" (for 64bit)

Example of "R.Net" in Ironpython script.  
The library of C# is used. Requires VisualStudio 2017 or higher.

## File

* "wk_rdotnet_ipy" folder.
  * There are IronPython script files.
  * Run "example.py".
* "wk_rdotnet.sln"
  * To install "R.NET".
  * To generate "rdotnet" package.

## Notes on execution

* Open "wk_rdotnet.sln".
* Install "R.NET" with NuGet.
* Build.
* Copy the "x64/debug/rdotnet" or "x64/release/rdotnet" folder to IronPython's "Lib" folder.
* Environment variable "IRONPYTHON_HOME" and "R_HOME" required. They are installation location.
* Open "wk_rdotnet_ipy" folder with Visual Studio Code and run "example.py".
  * You need the Python extension created by Don Jayamanne.
  * Edit "python.pythonPath" in "settings.json" in the ".vscod" folder to the appropriate path. The following is a description for IronPython 2.7.9.

```
"python.pythonPath": "C:/Program Files/IronPython 2.7/ipy.exe"
```
