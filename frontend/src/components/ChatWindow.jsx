import { Bot, User } from "lucide-react";

function ChatWindow({ messages, loading, status }) {
  if (messages.length === 0) {
    return (
      <div className="flex flex-1 items-center justify-center">
        <div className="max-w-xl text-center">

          <h1 className="text-4xl font-semibold tracking-tight">
            What do you want to research?
          </h1>

          <p className="mt-3 text-muted-foreground">
            Ask Shod a research question and explore relevant papers.
          </p>

        </div>
      </div>
    );
  }

  return (
    <div className="flex-1 overflow-y-auto px-6 py-8">

      <div className="mx-auto max-w-3xl space-y-8">

        {messages.map((message) => (
          <div
            key={message.id}
            className="flex gap-4"
          >

            <div className="mt-1 shrink-0">
              {message.role === "user" ? (
                <User size={20} />
              ) : (
                <Bot size={20} />
              )}
            </div>

            <div className="min-w-0 flex-1">
              <p className="mb-1 text-sm font-medium">
                {message.role === "user" ? "You" : "Shod"}
              </p>

              <div className="whitespace-pre-wrap text-sm leading-7">
                {message.content}
              </div>
            </div>

          </div>
        ))}

        {loading && (
          <div className="flex gap-4">
            <div className="mt-1">
              <Bot size={20} />
            </div>

            <div>
              <p className="mb-1 text-sm font-medium">
                Shod
              </p>

              <p className="text-sm text-muted-foreground">
                {status || "Thinking..."}
              </p>
            </div>
          </div>
        )}

      </div>

    </div>
  );
}

export default ChatWindow;