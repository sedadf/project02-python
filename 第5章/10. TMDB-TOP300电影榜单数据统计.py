"""
10. TMDB-TOP300电影榜单数据统计
参考: 第5章/09.TMDB-TOP 300电影磅单分析.ipynb
功能: 对TMDB TOP300电影数据从年份、语言、类型、评分四个维度进行统计分析并绘制图表
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# 展示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据文件路径
DATA_PATH = "data/movies.csv"
# 输出图片路径
OUTPUT_PATH = "data/TMDB-TOP 300.png"


def load_data(path: str) -> pd.DataFrame:
    """加载电影数据，只保留需要的列，并处理年份缺失值。

    Args:
        path: CSV 文件路径

    Returns:
        处理后的 DataFrame
    """
    data = pd.read_csv(
        path,
        usecols=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言"],
        dtype={"年份": "Int64"},
    )
    # 缺失年份时，从上映时间前4位提取年份进行填充
    data["年份"] = data["年份"].fillna(data["上映时间"].str[:4])
    return data


def create_figure() -> tuple[Figure, list[Axes]]:
    """创建 2x2 子图画布并返回画布与子图列表。

    Returns:
        (fig, axes_list): 画布对象与扁平化的子图列表
    """
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle("TMDB-TOP 300电影磅单分析", fontsize=20, x=0.5, y=0.98)
    fig.subplots_adjust(hspace=0.5, wspace=0.3)
    # 将 2x2 数组展平为一维列表，方便按索引访问
    axes_list: list[Axes] = [axes[0][0], axes[0][1], axes[1][0], axes[1][1]]
    return fig, axes_list


def draw_year_chart(ax: Axes, data: pd.DataFrame) -> None:
    """需求1：绘制每年上映电影数量变化的折线图。

    Args:
        ax: 目标子图
        data: 电影数据
    """
    # 分组统计每年电影数量
    year_count: pd.Series = data.groupby("年份")["年份"].count()

    # 构建连续的 x 轴（年份）与对应的 y 轴（数量）
    min_year: int = int(year_count.index.min())
    max_year: int = int(year_count.index.max())
    x = list(range(min_year, max_year + 1))
    y = [int(year_count.get(i, 0)) for i in x]

    ax.plot(x, y)
    ax.set_title("每年上映电影数量变化", fontsize=16)
    ax.set_xlabel("年份", fontsize=14)
    ax.set_ylabel("电影数量", fontsize=14)
    ax.set_xticks(x[::10])          # x 轴每隔10年显示刻度
    ax.set_yticks(list(range(0, 31, 3)))  # y 轴每隔3显示刻度
    ax.grid(linestyle="--", alpha=0.5)


def draw_language_chart(ax: Axes, data: pd.DataFrame) -> None:
    """需求2：绘制不同语言对应电影数量的柱状图。

    Args:
        ax: 目标子图
        data: 电影数据
    """
    # 分组统计并按数量降序排列
    language_count: pd.Series = (
        data.groupby("语言")["语言"].count().sort_values(ascending=False)
    )

    x_language = language_count.index.tolist()
    y_count = language_count.values.tolist()

    ax.bar(x_language, y_count, color="r", width=0.5)
    ax.set_title("不同语言对应电影数量", fontsize=16)
    ax.set_xlabel("语言", fontsize=14)
    ax.set_ylabel("电影数量", fontsize=14)
    ax.grid(linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", rotation=90)  # x 轴刻度旋转90度，避免重叠


def draw_type_chart(ax: Axes, data: pd.DataFrame) -> None:
    """需求3：绘制不同类型对应电影数量的柱状图。

    每部电影可以有多个类型（逗号分隔），分别统计每个类型的出现次数。

    Args:
        ax: 目标子图
        data: 电影数据
    """
    type_count: dict[str, int] = {}
    for types in data["类型"].str.split(","):
        for t in types:
            type_count[t] = type_count.get(t, 0) + 1

    x_types = list(type_count.keys())
    y_values = list(type_count.values())

    ax.bar(x_types, y_values, color="r", width=0.5)
    ax.set_title("不同类型对应电影数量", fontsize=16)
    ax.set_xlabel("类型", fontsize=14)
    ax.set_ylabel("电影数量", fontsize=14)
    ax.grid(linestyle="--", alpha=0.5)
    ax.tick_params(axis="x", rotation=90)


def draw_score_chart(ax: Axes, data: pd.DataFrame) -> None:
    """需求4：绘制不同评分电影占比的饼图。

    占比小于 2% 的评分合并为"其他"类别，避免饼图碎片过多。

    Args:
        ax: 目标子图
        data: 电影数据
    """
    score_count: pd.Series = data.groupby("评分")["评分"].count()

    total = score_count.sum()
    # 占比 >= 2% 的单独展示
    large_scores: pd.Series = score_count[score_count >= total * 0.02].copy()
    # 占比 < 2% 的合并为"其他"
    small_scores: pd.Series = score_count[score_count < total * 0.02]
    if small_scores.shape[0] > 0:
        large_scores["其他"] = small_scores.sum()

    labels = large_scores.index.tolist()
    values = large_scores.values.tolist()

    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=0, radius=1.2)
    ax.set_title("不同评分电影占比", fontsize=16)
    ax.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.3))


def main() -> None:
    """主函数：加载数据，创建画布，依次绘制四张图表并保存。"""
    data = load_data(DATA_PATH)
    fig, axes = create_figure()

    draw_year_chart(axes[0], data)
    draw_language_chart(axes[1], data)
    draw_type_chart(axes[2], data)
    draw_score_chart(axes[3], data)

    plt.savefig(OUTPUT_PATH)
    plt.show()
    print(f"图表已保存至: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
