class NodeURL:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = NodeURL(homepage)
        self.index = 1
        self.length = 1

    def visit(self, url: str) -> None:
        new_node_url = NodeURL(url)
        if not self.length:
            self.current = new_node_url
        elif self.index < self.length:
            self.current.next = new_node_url
            new_node_url.prev = self.current
            self.current = new_node_url
            self.length = self.index
        else:
            self.current.next = new_node_url
            new_node_url.prev = self.current
            self.current = new_node_url
        self.index += 1
        self.length += 1

    def back(self, steps: int) -> str:
        valid_steps = min(steps, self.index - 1)
        for i in range(valid_steps):
            self.current = self.current.prev
            self.index -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        max_range = self.length - self.index
        valid_steps = min(steps, max_range)  # Use min to ensure valid steps
        for i in range(valid_steps):
            self.current = self.current.next
            self.index += 1
        return self.current.val