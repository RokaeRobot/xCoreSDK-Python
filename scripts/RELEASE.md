# 发版：Python 预编译库 / Release: Prebuilt Libraries

## 发版流程

1. 确认 `rokae_SDK_*_v<version>_py38/lib/` 下库文件齐全
2. 打包：`.\scripts\package_libs.ps1 -Version 0.1.6`
3. 推送源码并打 tag：`git tag v0.1.6 && git push origin main && git push origin v0.1.6`
4. 上传 `dist/*` 到 https://github.com/RokaeRobot/xCoreSDK-Python/releases

```bash
gh release create v0.1.6 dist/* --title "v0.1.6"
```

**勿将** `lib/*.so` / `lib/*.pyd` 提交到 Git。
