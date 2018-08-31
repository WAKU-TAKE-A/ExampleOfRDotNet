# Example of R.Net (for 64bit)

Example of R.Net in Ironpython script.  
The library of C# is used.

## File

* `wk_rdotnet_ipy` folder.
  * There are IronPython script files.
  * Run `example_wk_rdotnet.py`.
* `wk_rdotnet.sln`
  * To install R.NET.
  * To generate `rdotnet` package.

## Notes on execution

* Open `wk_rdotnet.sln`.
* Install R.NET with NuGet.
* Build.
  * What is needed is only the `__init__.py`, `rdotnet.html`, `DynamicInterop.dll`, `RDotNet.dll` and `RDotNet.NativeLibrary.dll`.
* Copy the `x64_debug/rdotnet` or `x64_release/rdotnet` folder to IronPython's `Lib` folder.
* Open `wk_rdotnet_ipy` folder with `Visual Studio Code` and run `example_wk_rdotnet.py`.
  * You need the `Python` extension created by Don Jayamanne.
  * Edit `python.pythonPath` in `settings.json` in the `.vscod` folder to the appropriate path. The following is a description for IronPython 2.7.8.

```
"python.pythonPath": "C:/Program Files/IronPython 2.7/ipy.exe"
```
