# git命令

## 创建

### 初始化一个Git仓库

* git init
* git clone

### 添加文件到Git仓库

* git add `<file>` 或 git add .  添加全部
* git commit

## 本地提交修改

### 仓库当前状态

* git status

### 查看修改内容

* git diff

### 历史记录

* git log

### 回退到上个版本

* git reset --hard HEAD^

### 查看本地版本提交记录命令历史

* git reflog

### 用版本库里的版本替换工作区的版本(通常用于丢弃工作区的修改和恢复误删文件)

* git checkout -- file

### 撤销暂存区的修改

* git reset HEAD file

### 从版本库删除文件

* git rm file

## 远程仓库

### 添加远程仓库

* git remote add origin git@github.com:xxx/xxxx.git  
  其中origin为远程仓库名,可以任意替换

### 推送到远程库

* git push -u origin master  
  -u参数关联本地master和远程master分支  
  以后推送或拉取时可以简化命令

### 查看远程库信息

* git remote -v
* git remote show origin

## 分支管理

### 创建并切换分支

* git checkout -b dev  
等同于git branch dev 和 git checkout dev

### 查看分支

* git branch  
  加-a参数能看远程库分支

### 合并指定分支到当前分支

* git merge dev  
  不加参数默认fast forward模式

* git merge dev --no-ff  
  用普通模式合并,合并后的历史有分支,能看出曾经做过合并

### 删除分支

* git branch -d dev

### 工作区封存

* git stash
* git stash list
* git stash apply `<stash@{0}>`
* git stash drop
* git stash pop

### 创建远程origin的dev分支到本地

* git checkout -b dev origin/dev

### 指定本地dev分支与远程origin/dev分支的链接

* git branch --set-upstream dev origin/dev

## 标签管理

### 打标签

* git tag `<name>`  
在当前分支的最新提交的committee上
* git tag `<name>` `<commit_id>`
* git -a v0.1 -m "version 0.1 released" 3628164  
  -a指定标签名 -m指定说明文字

### 删除标签

* git tag -d v0.1

### 推送某个标签到远程

* git push origin v0.1
* git push origin --tags  
    推送全部

### 查看远程标签

* git ls-remote --tags

### 删除推送到远程的标签

* git tag -d v0.1  
  先删本地
* git push origin :refs/tags/v0.1  
  再从远程删除
* git push origin --delete tag v0.1  
  直接删除

![](http://7xl5zf.com1.z0.glb.clouddn.com/git_help.bmp)
