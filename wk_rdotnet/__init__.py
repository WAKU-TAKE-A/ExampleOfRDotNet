# -*- coding: utf-8 -*-

"""
Package for using R language on IronPython

* It is for 64 bit.
* Set the path of R_HOME and IRONPYTHON_HOME.
* RDotNet.dll, RDotNet.NativeLibrary.dll and DynamicInterop.dll is required.
https://www.nuget.org/packages/R.NET.Community/
"""

__author__  = "Nishida Takehito <takehito.nishida@gmail.com>"
__version__ = "0.9.10.0"
__date__    = "2018/11/5"

#
# Set path.
#
import os
import clr
import os.path as path
from sys import path as systemPath
from System import Environment as env
IRONPYTHON_HOME = env.GetEnvironmentVariable("IRONPYTHON_HOME")
R_HOME = env.GetEnvironmentVariable("R_HOME")

if IRONPYTHON_HOME is None or R_HOME is None:
    raise Exception("Error : Set path of R_HOME and IRONPYTHON_HOME.")

IRONPYTHON_RDOTNET = path.join(IRONPYTHON_HOME, "Lib\\rdotnet")
systemPath.append(IRONPYTHON_RDOTNET)
systemPath.append(R_HOME)
print("R : " + R_HOME)
print("rdotnet : " + IRONPYTHON_RDOTNET)

#
# Add reference.
#
clr.AddReferenceToFile("RDotNet.dll")
import RDotNet
from RDotNet import REngineExtension
from RDotNet import SymbolicExpressionExtension

#
# Initialize.
#
RDotNet.REngine.SetEnvironmentVariables(path.join(R_HOME, "bin\\x64"), R_HOME)
Engine = RDotNet.REngine.GetInstance()
_r_print = SymbolicExpressionExtension.AsFunction(Engine.Evaluate("print"))
print("REngine is initialized.")

#
# Functions.
#
def Initialize():
    """
    Initialize REngine.
    """
    global Engine
    if Engine is None:
        RDotNet.REngine.SetEnvironmentVariables(path.join(R_HOME, "bin\\x64"), R_HOME)
        Engine = RDotNet.REngine.GetInstance()
        print("REngine is initialized.")
    else:
        print("REngine has already been initialized.")
    

def runPrint(var):
    """
    Run print command.
    
    var : The SymbolicExpression.
    """
    _r_print = SymbolicExpressionExtension.AsFunction(Engine.Evaluate("print"))
    runFunction(_r_print, [var])

def runFunction(func, opt, type=None, enToArray=False):
    """
    Run the function.
    
    func : The function.
    ops : List of SymbolicExpression.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    enToArray : if enToArray is True, run Vector.ToArray().
    return : The SymbolicExpression.
    """
    dst = convert(func.__getattribute__("Invoke")(tuple(opt)), type)
    if enToArray:
        dst = runToArray(dst)
    return dst

def runFunc(func, opt, type=None, enToArray=False):
    """
    Same as runFunction().
    """
    return runFunction(func, opt, type, enToArray)

def runLength(var):
    """
    Run Vector.Lengh.
    
    var : The SymbolicExpression.
    """
    return var.__getattribute__("Length")

def runToArray(var):
    """
    Run Vector.ToArray().
    
    var : The SymbolicExpression.
    """
    return var.__getattribute__("ToArray")()

def showDoc():
    """
    Show the document of rdotnet package.
    """
    import webbrowser
    webbrowser.open("file:///" + path.join(RDOTNET_PATH, "rdotnet.html"))

def getSymbol(name, type=None, enToArray=False):
    """
    Get a symbol defined in the global environment.
    
    name : The name.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    enToArray : if enToArray is True, run Vector.ToArray().
    return : The SymbolicExpression.
    """
    global Engine
    dst = convert(Engine.GetSymbol(name), type)
    if enToArray:
        dst = runToArray(dst)
    return dst

def setSymbol(name, var):
    """
    Assign a value to a name in the global environment.
    
    name : The name.
    var : The SymbolicExpression.
    """
    global Engine
    Engine.SetSymbol(name, var)

def evaluate(cmd, type=None, enToArray=False):
    """
    Evaluate a statement in the given stream.
    
    cmd : The given string.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    enToArray : if enToArray is True, run Vector.ToArray().
    return : The SymbolicExpression.
    """
    global Engine
    dst = convert(Engine.Evaluate(cmd), type)
    if enToArray:
        dst = runToArray(dst)
    return dst

def eval(cmd, type=None, enToArray=False):
    """
    Same as evaluate().
    """
    return evaluate(cmd, type, enToArray)

def convert(var, type):
    """
    Get the SymbolicExpression as the given type.
    
    var : The SymbolicExpression.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    retuen : The converted SymbolicExpression.
    """
    if type is None or type == "":
        return var
    elif type == "Character" or type == "character":
        if isMatrix(var):
            return asCharacterMatrix(var)
        else:
            return asCharacter(var)
    elif type == "Complex" or type == "complex":
        if isMatrix(var):
            return asComplexMatrix(var)
        else:
            return asComplex(var)
    elif type == "DataFrame" or type == "dataframe":
        return asDataFrame(var)
    elif type == "Environment" or type == "environment":
        return asEnvironment(var)
    elif type == "Expression" or type == "expression":
        return asExpression(var)
    elif type == "Factor" or type == "factor":
        return asFactor(var)
    elif type == "Function" or type == "function":
        return asFunction(var)
    elif type == "Integer" or type == "integer":
        if isMatrix(var):
            return asIntegerMatrix(var)
        else:
            return asInteger(var)
    elif type == "Language" or type == "language":
        return asLanguage(var)
    elif type == "List" or type == "list":
        return asList(var)
    elif type == "Logical" or type == "logical":
        if isMatrix(var):
            return asLogicalMatrix(var)
        else:
            return asLogical(var)
    elif type == "Numeric" or type == "numeric":
        if isMatrix(var):
            return asNumericMatrix(var)
        else:
            return asNumeric(var)
    elif type == "Raw" or type == "raw":
        if isMatrix(var):
            return asRawMatrix(var)
        else:
            return asRaw(var)
    elif type == "S4" or type == "s4":
        return asS4(var)
    elif type == "Symbol" or type == "symbol":
        return asSymbol(var)
    elif type == "Vector" or type == "vector":
        return asVector(var)
    else:
        raise Exception("Error : There is no such type.")

def asCharacter(var):
    return SymbolicExpressionExtension.AsCharacter(var)

def asCharacterMatrix(var):
    if isMatrix(var):
        return SymbolicExpressionExtension.AsCharacterMatrix(var)
    else:
        return var

def asComplex(var):
    return SymbolicExpressionExtension.AsComplex(var)

def asComplexMatrix(var):
    if isMatrix(var):
        return SymbolicExpressionExtension.AsComplexMatrix(var)
    else:
        return var

def asDataFrame(var, colnames=None):
    if isDataFrame(var):
        return SymbolicExpressionExtension.AsDataFrame(var)
    elif isMatrix(var):
        asdf = evaluate("as.data.frame", "function")
        dst = runFunction(asdf, [var], "dataframe")
        asdf.Dispose()
        return dst
    else:
        return var

def asEnvironment(var):
    if isEnvironment(var):
        return SymbolicExpressionExtension.AsEnvironment(var)
    else:
        return var

def asExpression(var):
    if isExpression(var):
        return SymbolicExpressionExtension.AsExpression(var)
    else:
        return var

def asFactor(var):
    if isFactor(var):
        return SymbolicExpressionExtension.AsFactor(var)
    else:
        return var

def asFunction(var):
    if isFunction(var):
        return SymbolicExpressionExtension.AsFunction(var)
    else:
        return var

def asInteger(var):
    return SymbolicExpressionExtension.AsInteger(var)

def asIntegerMatrix(var):
    if isMatrix(var):
        return SymbolicExpressionExtension.AsIntegerMatrix(var)
    else:
        return var

def asLanguage(var):
    if isLanguage(var):
        return SymbolicExpressionExtension.AsLanguage(var)
    else:
        return var

def asList(var):
    if isList(var):
        return SymbolicExpressionExtension.AsList(var)
    else:
        return var

def asLogical(var):
    return SymbolicExpressionExtension.AsLogical(var)

def asLogicalMatrix(var):
    if isMatrix(var):
        return SymbolicExpressionExtension.AsLogicalMatrix(var)
    else:
        return var

def asNumeric(var):
    return SymbolicExpressionExtension.AsNumeric(var)

def asNumericMatrix(var):
    if isMatrix(var):
        return SymbolicExpressionExtension.AsNumericMatrix(var)
    else:
        return var

def asRaw(var):
    return SymbolicExpressionExtension.AsRaw(var)

def asRawMatrix(var):
    if isMatrix(var):
        return SymbolicExpressionExtension.AsRawMatrix(var)
    else:
        return var

def asS4(var):
    if isS4(var):
        return SymbolicExpressionExtension.AsS4(var)
    else:
        return var

def asSymbol(var):
    if isSymbol(var):
        return SymbolicExpressionExtension.AsSymbol(var)
    else:
        return var

def asVector(var):
    if isVector(var):
        return SymbolicExpressionExtension.AsVector(var)
    else:
        return var

def isDataFrame(var):
    return SymbolicExpressionExtension.IsDataFrame(var)

def isEnvironment(var):
    return SymbolicExpressionExtension.IsEnvironment(var)

def isExpression(var):
    return SymbolicExpressionExtension.IsExpression(var)

def isFactor(var):
    return SymbolicExpressionExtension.IsFactor(var)
    
def isFunction(var):
    return SymbolicExpressionExtension.IsFunction(var)

def isLanguage(var):
    return SymbolicExpressionExtension.IsLanguage(var)

def isList(var):
    return SymbolicExpressionExtension.IsList(var)

def isMatrix(var):
    return SymbolicExpressionExtension.IsMatrix(var)

def isS4(var):
    return SymbolicExpressionExtension.IsS4(var)

def isSymbol(var):
    return SymbolicExpressionExtension.IsSymbol(var)

def isVector(var):
    return SymbolicExpressionExtension.IsVector(var)

def createCharacterVector(var, name=None):
    global Engine
    dst = REngineExtension.CreateCharacterVector(Engine, var)
    if name != None:
        setSymbol(name, dst)
    return dst

def createComplexVector(var, name=None):
    global Engine
    dst = REngineExtension.CreateComplexVector(Engine, var)
    if name != None:
        setSymbol(name, dst)
    return dst

def createIntegerVector(var, name=None):
    global Engine
    dst = REngineExtension.CreateIntegerVector(Engine, var)
    if name != None:
        setSymbol(name, dst)
    return dst

def createLogicalVector(var, name=None):
    global Engine
    dst = REngineExtension.CreateLogicalVector(Engine, var)
    if name != None:
        setSymbol(name, dst)
    return dst

def createNumericVector(var, name=None):
    global Engine
    dst = REngineExtension.CreateNumericVector(Engine, var)
    if name != None:
        setSymbol(name, dst)
    return dst

def createRawVector(var, name=None):
    global Engine
    dst = REngineExtension.CreateRawVector(Engine, var)
    if name != None:
        setSymbol(name, dst)
    return dst

def createCharacterMatrix(row, col, name=None):
    global Engine
    dst = REngineExtension.CreateCharacterMatrix(Engine, row, col)
    if name != None:
        setSymbol(name, dst)
    return dst

def createComplexMatrix(row, col, name=None):
    global Engine
    dst = REngineExtension.CreateComplexMatrix(Engine, row, col)
    if name != None:
        setSymbol(name, dst)
    return dst

def createIntegerMatrix(row, col, name=None):
    global Engine
    dst = REngineExtension.CreateIntegerMatrix(Engine, row, col)
    if name != None:
        setSymbol(name, dst)
    return dst

def createLogicalMatrix(row, col, name=None):
    global Engine
    dst = REngineExtension.CreateLogicalMatrix(Engine, row, col)
    if name != None:
        setSymbol(name, dst)
    return dst

def createNumericMatrix(row, col, name=None):
    global Engine
    dst = REngineExtension.CreateNumericMatrix(Engine, row, col)
    if name != None:
        setSymbol(name, dst)
    return dst

def createRawMatrix(row, col, name=None):
    global Engine
    dst = REngineExtension.CreateRawMatrix(Engine, row, col)
    if name != None:
        setSymbol(name, dst)
    return dst

def createDataFrame(list_vec, colnames=None, name=None):
    """
    Create the DataFrame.
    
    list_vec : The list of RDotNet.Vector.
    colnames : The list of IronPython.
    return : The expression.
    """
    if list_vec is None or len(list_vec) == 0:
        return None
    if colnames is None or len(list_vec) != len(colnames):
        colnames = []
        for i in xrange(len(list_vec)):
            colnames.append("V{0}".format(i + 1))
    _r_dataframe = SymbolicExpressionExtension.AsFunction(Engine.Evaluate("data.frame"))
    _r_colnames = SymbolicExpressionExtension.AsFunction(Engine.Evaluate("colnames"))
    dst = runFunction(_r_dataframe, list_vec, "dataframe")
    cln = runFunction(_r_colnames, [dst], "character")
    for i in xrange(len(list_vec)):
        cln[i] = colnames[i]
    if name != None:
        setSymbol(name, dst)
    return dst
