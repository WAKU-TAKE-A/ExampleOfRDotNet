# -*- coding: utf-8 -*-

"""
rdotnet.

* It is for 64 bit.
* Set the path of R_HOME and IRONPYTHON_HOME.
* RDotNet.dll, RDotNet.NativeLibrary.dll and DynamicInterop.dll is required.
https://www.nuget.org/packages/R.NET.Community/
"""

__author__  = "Nishida Takehito <takehito.nishida@gmail.com>"
__version__ = "0.9.6.0"
__date__    = "2018/8/31"

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

RDOTNET_PATH = path.join(IRONPYTHON_HOME, "Lib\\rdotnet")
systemPath.append(RDOTNET_PATH)
systemPath.append(R_HOME)
print("R : " + R_HOME)
print("rdotnet : " + RDOTNET_PATH)

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
print("REngine is initialized.")

#
# Functions.
#
def runFunction(func, opt, type=None):
    """
    Run a function.
    
    func : The function.
    ops : List of expression.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    return : The expression.
    """
    return convert(func.__getattribute__("Invoke")(tuple(opt)), type)

def showDoc():
    """
    Show the document.
    """
    import webbrowser
    webbrowser.open("file:///" + path.join(RDOTNET_PATH, "rdotnet.html"))

def getSymbol(name, type=None):
    """
    Gets a symbol defined in the global environment.
    
    name : The name.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    return : The expression.
    """
    global Engine
    return convert(Engine.GetSymbol(name), type)

def setSymbol(name, var):
    """
    Assign a value to a name in the global environment.
    
    name : The name.
    var : The expression.
    """
    global Engine
    Engine.SetSymbol(name, var)

def evaluate(cmd, type=None):
    """
    Evaluates a statement in the given stream.
    
    cmd : The given string.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    return : The expression.
    """
    global Engine
    return convert(Engine.Evaluate(cmd), type)

def eval(cmd, type=None):
    global Engine
    return convert(Engine.Evaluate(cmd), type)

def convert(var, type):
    """
    Get the expression as the given type.
    
    var : The expression.
    type : If type is not None, run RDotNet.SymbolicExpressionExtension.As***().
    retuen : The converted expression.
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

def createCharacterVector(var):
    global Engine
    return REngineExtension.CreateCharacterVector(Engine, var)

def createComplexVector(var):
    global Engine
    return REngineExtension.CreateComplexVector(Engine, var)

def createIntegerVector(var):
    global Engine
    return REngineExtension.CreateIntegerVector(Engine, var)

def createLogicalVector(var):
    global Engine
    return REngineExtension.CreateLogicalVector(Engine, var)

def createNumericVector(var):
    global Engine
    return REngineExtension.CreateNumericVector(Engine, var)

def createRawVector(var):
    global Engine
    return REngineExtension.CreateRawVector(Engine, var)

def createCharacterMatrix(row, col):
    global Engine
    return REngineExtension.CreateCharacterMatrix(Engine, row, col)

def createComplexMatrix(row, col):
    global Engine
    return REngineExtension.CreateComplexMatrix(Engine, row, col)

def createIntegerMatrix(row, col):
    global Engine
    return REngineExtension.CreateIntegerMatrix(Engine, row, col)

def createLogicalMatrix(row, col):
    global Engine
    return REngineExtension.CreateLogicalMatrix(Engine, row, col)

def createNumericMatrix(row, col):
    global Engine
    return REngineExtension.CreateNumericMatrix(Engine, row, col)

def createRawMatrix(row, col):
    global Engine
    return REngineExtension.CreateRawMatrix(Engine, row, col)
