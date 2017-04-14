import System.Environment
import System.IO

readArgFile :: String -> IO Handle -- read file arguement
readArgFile path = openFile path ReadMode 

createBackup :: String -> IO Handle -- create a new file
createBackup path = openFile path WriteMode

main = do args <- getArgs
          oldFileHandle <- readArgFile (head args)
          backupFileHandle <- createBackup ((head args) ++ ".bak")
          contents <- hGetContents oldFileHandle
          putStr contents
          hPutStr backupFileHandle contents
          
          hClose oldFileHandle
          hClose backupFileHandle

    

