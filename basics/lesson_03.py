# Auto Generated Agent Chat: Collaborative Task Solving with Multiple Agents and Human Users

import autogen


config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
    },
)


def ask_expert(message):
    assistant_for_expert = autogen.AssistantAgent(
        name="assistant_for_expert",
        llm_config={
            "temperature": 0,
            "config_list": config_list,
        },
    )

    expert = autogen.UserProxyAgent(
        name="expert",
        human_input_mode="ALWAYS",
        code_execution_config={
            "work_dir": "expert",
            "use_docker": False,
        },
    )

    expert.initiate_chat(
        assistant_for_expert,
        message=message
    )

    expert.stop_reply_at_receive(sender=assistant_for_expert)

    expert.send(
        "summarize the solution and explain the answer in an easy-to-understand way", assistant_for_expert)

    # return the last message the expert received
    return expert.last_message()["content"]


assistant_for_student = autogen.AssistantAgent(
    name="student_assistant",
    llm_config={
        "timeout": 600,
        "config_list": config_list,
        "temperature": 0,
        "functions": [
            {
                "name": "ask_expert",
                "description": "ask expert when you can't solve the problem satisfactorily.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "question to ask expert. Ensure the question includes enough context, such as the code and the execution result. The expert does not know the conversation between you and the user unless you share the conversation with the expert.",
                        },
                    },
                    "required": ["message"],
                },
            }
        ],
    }
)

student = autogen.UserProxyAgent(
    name="student",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "student",
        "use_docker": False,
    },
    function_map={"ask_expert": ask_expert},
)

student.initiate_chat(
    assistant_for_student,
    message="""Find $a + b + c$, given that $x+y \\neq -1$ and 
\\begin{align}
	ax + by + c & = x + 7,\\
	a + bx + cy & = 2x + 6y,\\
	ay + b + cx & = 4x + y.
\\end{align}.
""",
)
