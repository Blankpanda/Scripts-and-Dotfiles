(when (>= emacs-major-version 24)
(require 'package)
(add-to-list
  'package-archives
   '("melpa" . "http://melpa.org/packages/")
   t)
  (package-initialize))


;; setup
(setq initial-scratch-message "")
(setq inhibit-startup-message t)
(setq visible-bell t)
(scroll-bar-mode 0)
(menu-bar-mode 0)
(tool-bar-mode 0)
(fringe-mode 4)
; (setq pop-up-frames t)

;; scroll with mousewheel
(mouse-wheel-mode 1)
;; stop cursor blink
(blink-cursor-mode 0)
;; rebind C-c, C-x, C-v
(cua-mode 1)
;; auto complete parenthesis
(electric-pair-mode 1)
;; text wrapping
(global-visual-line-mode 1)
(require 'font-lock)
(global-hi-lock-mode nil)
;; i-beam cursor
(modify-all-frames-parameters (list (cons 'cursor-type 'bar)))
;; no line numbers
(global-linum-mode 1)
;; easier windows movement (<SHIFT> + ARROW KEYS)
(when (fboundp 'windmove-default-keybindings)
  (windmove-default-keybindings 'meta))


;; theme
(load-theme 'leuven t)
