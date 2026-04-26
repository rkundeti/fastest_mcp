        children = structured_content["view"]["children"]
        for col in children:
            for child in col.get("children", []):
                for item in child.get("children", []):
                    if item.get("type") == "DataTable":
                        return item.get("rows")
    except (KeyError, TypeError):
        pass
    return None
def format_team_table(members: list[dict]) -> str:
    """Render members as a plain-text table."""
    lines = [
        f"{'Name':<18} {'Role':<22} {'Office':<15} {'Projects'}",
        "-" * 65,
    ]
    for m in members:
        lines.append(
            f"{m['name']:<18} {m['role']:<22} {m['office']:<15} {m['projects']}"
        )
    return "\n".join(lines)
async def call_mcp_tool(mcp_client: Client, name: str, args: dict) -> str:
    result = await mcp_client.call_tool(name, args)
    # team_directory returns a Prefab UI payload — extract the member table
    if name == "team_directory":
        members = None
        if result.data:
            members = extract_members(result.data)
Now run it:

.venv\Scripts\python.exe ollama_chat_client.py
Here's how it works end-to-end:

Connected — 1 tool(s): ['team_directory']
Team Directory Chatbot  (type 'quit' to exit)
You: show me the team
  [calling tool: team_directory]