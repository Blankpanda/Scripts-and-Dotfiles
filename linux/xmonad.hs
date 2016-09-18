import XMonad
import XMonad.Layout.Spacing
import XMonad.Config.Xfce
import XMonad.Layout.ResizableTile
import XMonad.Config.Desktop
import XMonad.Util.EZConfig (additionalKeys)
import XMonad.Hooks.ManageDocks

--
-- Useful imports
--
import XMonad.Core as XMonad hiding
    (workspaces,manageHook,keys,logHook,startupHook,borderWidth,mouseBindings
    ,layoutHook,modMask,terminal,normalBorderColor,focusedBorderColor,focusFollowsMouse
    ,handleEventHook,clickJustFocuses)
import qualified XMonad.Core as XMonad
    (workspaces,manageHook,keys,logHook,startupHook,borderWidth,mouseBindings
    ,layoutHook,modMask,terminal,normalBorderColor,focusedBorderColor,focusFollowsMouse
    ,handleEventHook,clickJustFocuses)

import XMonad.Layout
import XMonad.Operations
import XMonad.ManageHook
import qualified XMonad.StackSet as W
import Data.Bits ((.|.))
import Data.Monoid
import qualified Data.Map as M
import System.Exit
import Graphics.X11.Xlib
import Graphics.X11.Xlib.Extras

myWorkspaces = map show [1 .. 2 :: Int]
myFocusedBorderColor = "#ffffff"
myNormalBorderColor = "#000000"

myLayout = tiled ||| Full
  where
    tiled = spacing 15 $ Tall nmaster delta ratio
    nmaster = 1
    ratio = 1/2
    delta = 5/100

myLayoutHook = spacing 2 $ Tall 1 (3/100) (1/2)
myBorderWidth = 1

main = xmonad xfceConfig
    { terminal           = "terminator"
    , modMask            = mod4Mask
    , workspaces         = myWorkspaces
    , normalBorderColor  = myNormalBorderColor
    , focusedBorderColor = myFocusedBorderColor
    , layoutHook         = myLayout
    , borderWidth        = myBorderWidth
    }
