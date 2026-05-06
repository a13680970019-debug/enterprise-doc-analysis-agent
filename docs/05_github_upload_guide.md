# GitHub 上传链路

## 方法一：网页直接上传

适合第一次上传。

1. 打开 GitHub
2. 点击右上角 `+`
3. 点击 `New repository`
4. Repository name 填：

```text
enterprise-doc-analysis-agent
```

5. 建议选择 `Private`
6. 点击 `Create repository`
7. 进入仓库后点击 `Add file`
8. 点击 `Upload files`
9. 将本项目文件夹中的所有文件拖进去
10. 点击 `Commit changes`

## 方法二：命令行上传

进入本项目文件夹：

```bash
cd enterprise-doc-analysis-agent
```

初始化 Git：

```bash
git init
git add .
git commit -m "Initial commit: enterprise document analysis agent"
```

绑定远程仓库：

```bash
git branch -M main
git remote add origin https://github.com/你的用户名/enterprise-doc-analysis-agent.git
git push -u origin main
```

## 注意事项

不要上传：

- 客户资料
- 合同原文
- API Key
- `.env`
- 内部数据库
- 真实商业报价
- 真实客户线索
