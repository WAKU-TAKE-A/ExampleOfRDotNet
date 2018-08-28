# Example of R.Net (for 64bit)

Example of R.Net in Ironpython script.  
The library of C# is used.

## File

* `wk_rdotnet_ipy` folder.
  * There are IronPython script files.
  * Run this `example_wk_rdotnet.py` file.
* `wk_rdotnet.sln`
  * A class that implements RDotNet.
  * `wk_rdotnet` is a related folder.

## Notes on execution.

* Open `wk_rdotnet.sln`, and build.
* Copy the "x64 / Debug" or "x64 / Release" folder to IronPython's "Lib" folder and change it to the folder name "rdotnet".
* Open `wk_rdotnet_ipy` folder with `Visual Studio Code` and execute it.
  * You need the `Python` extension created by Don Jayamanne.
  * Edit `python.pythonPath` in` settings.json` in the `.vscod` folder to the appropriate path. The following is a description for IronPython 2.7.8.

```
"python.pythonPath": "C:/Program Files/IronPython 2.7/ipy.exe"
```
