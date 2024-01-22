let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/home/python_projects/novel_scraper
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
tabnext 1
badd +23 database_module.py
badd +1 /mnt/g/Projects/Python_projects/novel_web_scraping/kgm/database_module_kgm.py
badd +1 ursl_db.py
badd +15 structured_urls.py
badd +126 /mnt/g/Projects/Python_projects/novel_web_scraping/kgm/beautifulsoup_module_kgm.py
badd +99 ~/.vimrc
badd +2 bs4_module.py
badd +1 urls.html
badd +3 .env
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
let g:this_session = v:this_session
let g:this_obsession = v:this_session
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
