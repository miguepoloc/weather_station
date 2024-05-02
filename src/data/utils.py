from data.strategy import DaysNodesData, HoursNodesData, NodesDataStrategy, TotalNodesData


def get_strategy_format_data(format: str) -> NodesDataStrategy:
    format_options: dict = {
        "total": TotalNodesData(),
        "hour": HoursNodesData(),
        "day": DaysNodesData(),
    }
    return format_options.get(format, TotalNodesData())
