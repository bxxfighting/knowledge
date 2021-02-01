### 问题
一些常用的vim配置  

### 解决办法
```
set nocompatible
set number
set softtabstop=4
filetype on
set history=1000
syntax on
set tabstop=4
set shiftwidth=4
set showmatch
set vb t_vb=
set ruler
"set nohls
"set hlsearch
set hls
"代码下划线关闭
set nocursorline

highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/

iab xdate <c-r>=strftime("%d/%m/%y %H:%M:%S")<cr>

map ,cc :botright cope<cr>
map ,cn :cn<cr>
map ,cp :cp<cr>
map ,s :%s/ \+$//g<cr>
map ,p :!python ./%<cr>


map ,pp :setlocal paste!<cr>
set autoindent
set smartindent

let Grep_Skip_Dirs = '.git CVS SCCS .svn generated'
set grepprg=/bin/grep\ -nH

map ,ss :setlocal spell!<cr>

filetype plugin on

autocmd FileType help set ma
autocmd FileType help set noreadonly
autocmd BufWritePost ~/.vim/doc/* :helptags ~/.vim/doc


function! OpenFile ()
  let line = getline (".")
  exec "e ".line
endfunction

map ,r :call OpenFile ()<CR>

set hidden

map <Tab> :bn<CR>
map ,d :bd<cr>

set fo=croq

map ,t :Tlist<CR>

let g:load_doxygen_syntax=1

map ,k :!gref <cword><ENTER>

map ,n :NERDTreeToggle<CR>

map ,, :q<CR>
map ,f :q!<CR>

map ,e :e ~/.vim/vimrc<CR>

autocmd! bufwritepost vimrc source ~/.vim/vimrc

imap JJ <esc>
imap jj <esc>

set wildmenu

set expandtab
set shiftwidth=4
set tabstop=4

set dictionary+=~/.vim/dict/simple
set dictionary-=/usr/share/dict/words dictionary+=/usr/share/dict/words

set ic
set incsearch


set stl=%f\ %m\ %r\ Line:$l/%L[%p%%]\ Col:%c\ Buf:%n\ [%b][0x%B]

set laststatus=2

set cpoptions+=$

set textwidth=100

iab frm from

set showcmd

set fillchars=""

nmap <silent> ,cd :lcd %:h<CR>
nmap <silent> ,md :!mkdir -p %:p:h<CR>

set langmenu=zh_CN.UTF-8
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim
"set fileencodings=utf-8,gb2312,gbk,gb18030
set termencoding=utf-8
set encoding=prc

if has("multi_byte")
    set encoding=utf-8
    set termencoding=utf-8
    set formatoptions+=mM
    set fencs=utf-8,gbk

    if v:lang=~?'^\(zh\)\|\(ja\)\|\(ko\)'
        set ambiwidth=double
    endif

    if has("win32")
        source $VIMRUNTIME/delmenu.vim
        source $VIMRUNTIME/menu.vim
        language messages zh_CN.utf-8
    endif
endif


"下面这三个是一定要加上的，原样写上
set nocompatible              " be iMproved, required
filetype off                  " required
set rtp+=~/.vim/bundle/Vundle.vim

"下面这句来最后一个call vundle#end() 是相匹配的，就相当于一个是代表开始，一个代表结束，
"这两句，中间就放上我们要安装的插件。
call vundle#begin()

"就是在这里写上你要安装插件的信息，在README.md中写的内容都删除掉，它里面只是举例子，
"并不是我们真的要装那些，而且它的例子的内容是，告诉我们有多种方式安装插件，可以通过github，
"可以通过本地下载，我们这里只使用github来安装插件。由于我是要安装python的插件，这个插件
"在github的地址是：，那么我们怎么来设置呢
"使用Plugin 'rkulla/pydiction'，写上这句就可以了，后面的'rkulla/pydiction'，你可以
"发现，其实就是上面那个地址中的后面部分。

Plugin 'rkulla/pydiction'
"Plugin 'scrooloose/syntastic'
Bundle 'Valloric/YouCompleteMe'

"如果你还要安装其它的插件，那么就继续在这中间加上。

call vundle#end()

"下面这句也必须加上，这是文档中特别强调的。
filetype plugin indent on

"到这里就算是配置完成了。
let g:pydiction_location = '/home/buxingxing/.vim/bundle/pydiction/complete-dict'

"set statusline+=%#errormsg#
"set statusline+=%*

"let g:syntastic_always_populate_loc_list = 0
"let g:syntastic_auto_loc_list = 0
"let g:syntastic_check_on_open = 0
"let g:syntastic_check_on_wq = 0

au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif

inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i<CR><ESC>V<V<O<BS>
inoremap < <><ESC>i
inoremap ' ''<ESC>i
inoremap " ""<ESC>i

set foldenable
set cursorline
set autowrite
set magic

" Make cursor always on center of screen by default
if !exists('noalwayscenter')
    " Calculate proper scrolloff
    autocmd VimEnter,WinEnter,VimResized,InsertLeave * :let &scrolloff = float2nr(floor(winheight(0)/2)+1)
    autocmd InsertEnter * :let &scrolloff = float2nr(floor(winheight(0)/2))
    " Use <Enter> to keep center in insert mode, need proper scrolloff
    inoremap <CR> <CR><C-o>zz
endif
```
