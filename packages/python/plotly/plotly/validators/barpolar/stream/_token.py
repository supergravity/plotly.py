import _plotly_utils.basevalidators


class TokenValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="token", parent_name="barpolar.stream", **kwargs):
        super(TokenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            no_blank=kwargs.pop("no_blank", True),
            role=kwargs.pop("role", "info"),
            strict=kwargs.pop("strict", True),
            **kwargs
        )
