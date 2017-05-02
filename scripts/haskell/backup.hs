import System.Environment
import System.Directory
import System.IO

createBackup :: String -> IO
createBackup ""   = createDirectory "~/"
createBackup path = createDirectory "~/"

main = do args <- getArgs
          
          createBackup (args)

