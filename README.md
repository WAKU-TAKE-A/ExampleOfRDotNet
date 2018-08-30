# Example of R.Net (for 64bit)

Example of R.Net in Ironpython script.  
The library of C# is used.

## File

* `wk_rdotnet_ipy` folder.
  * There are IronPython script files.
  * Run `example_wk_rdotnet.py` file.
* `wk_rdotnet.sln`
  * A class that implements R.NET.
  * `__init__.py` and `rdotnet.html` are files for the package.

## Notes on execution

* Open `wk_rdotnet.sln`.
* Install R.NET with NuGet.
* Build.
* Copy the `x64_debug/rdotnet` or `x64_release/rdotnet` folder to IronPython's `Lib` folder.
* Open `wk_rdotnet_ipy` folder with `Visual Studio Code` and run `example_wk_rdotnet.py`.
  * You need the `Python` extension created by Don Jayamanne.
  * Edit `python.pythonPath` in `settings.json` in the `.vscod` folder to the appropriate path. The following is a description for IronPython 2.7.8.

```
"python.pythonPath": "C:/Program Files/IronPython 2.7/ipy.exe"
```
