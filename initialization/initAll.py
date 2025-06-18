import initialization.packageCheck
import os

def checkAll():
    result=True

    dependencies = ["yfinance"]
    exceptions = {"whats_imported": "true_lib_name"}
    
    for item in dependencies:
        initialization.packageCheck.checkPackage(item, exceptions)
    return result