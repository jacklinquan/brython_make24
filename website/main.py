from browser import document, html, window, console, bind  # type: ignore
from make24_solver import solve24

def main():
    # Header
    document <= html.NAV(
        html.DIV(
            html.DIV("Make 24", Class="brand-logo center"),
            Class="nav-wrapper container center",
        ),
        Class="teal",
        role="navigation",
    )

    # Leave some space
    document <= html.P()

    # Numbers
    document <= html.DIV(
        (
            html.DIV(
                html.A(
                    str((i + 1) * 2),
                    Class="dropdown-trigger btn center",
                    href="#",
                    data_target=f"num_dropdown_{i}",
                    Id=f"num_{i}",
                ),
                Class="col s3 center",
            )
            for i in range(4)
        ),
        Class="row",
    )

    # Number dropdown
    for i in range(4):
        document <= html.UL(
            (
                html.LI(
                    html.A(
                        str(j),
                        href="#!",
                        Id=f"num_dropdown_{i}_item_{j}",
                    ),
                )
                for j in range(1, 14)
            ),
            Id=f"num_dropdown_{i}",
            Class="dropdown-content",
        )

    for i in range(4):
        for j in range(1, 14):
            document[f"num_dropdown_{i}_item_{j}"].bind(
                "click",
                (lambda ev, i=i, j=j: setattr(document[f"num_{i}"], "text", str(j))),
            )

    # Leave some space
    document <= html.P()

    # `Go` button
    document <= html.DIV(
        html.BUTTON("Go!", Class="btn center", Id="go_btn"),
        Class="container center",
    )

    def get_make24_result_text():
        nums = [
            int(document[f"num_{i}"].text)
            for i in range(4)
        ]
        
        all_result_24 = solve24(*nums)

        result_text = f"With number(s) {nums}, "
        result_text += f"there is/are {len(all_result_24)} solution(s) in total:\n"
        result_text += "\n".join((str(item) for item in all_result_24))

        return result_text
    
    document["go_btn"].bind(
        "click",
        lambda ev: setattr(document["output"], "text", get_make24_result_text())
    )

    # Leave some space
    document <= html.P()

    document <= html.DIV(Class="divider")

    # Leave some space
    document <= html.P()

    # Output
    document <= html.P(Class="flow-text", Id="output")

    # Must do window.M.AutoInit() after all html being loaded!
    window.M.AutoInit()


if __name__ == "__main__":
    main()
