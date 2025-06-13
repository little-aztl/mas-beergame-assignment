import matplotlib.font_manager as fm

# 列出所有可用的字体
font_list = [f.name for f in fm.fontManager.ttflist]
# 筛选出包含 'Heiti' 或 'PingFang' 的字体
chinese_fonts = [font for font in font_list if 'Heiti' in font or 'PingFang' in font]
print(chinese_fonts)