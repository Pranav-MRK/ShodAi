import { useState } from "react";
import axios from "axios";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

function MainResearch() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [sources, setSources] = useState([]);
  const [threadId, setThreadId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const handleSubmit = async () => {
    if (!message.trim() || loading) {
      return;
    }

    const question = message.trim();

    const userMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: question,
    };

    setMessages((previous) => [
      ...previous,
      userMessage,
    ]);

    setMessage("");
    setLoading(true);
    setStatus("Researching...");

    try {
      const response = await axios.post(
        "http://localhost:8000/research",
        {
          question,
          thread_id: threadId,
        }
      );

      const data = response.data;

      setThreadId(data.thread_id);
      setSources(data.sources || []);

      const assistantMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: data.answer,
      };

      setMessages((previous) => [
        ...previous,
        assistantMessage,
      ]);

    } catch (error) {
      console.error("Research request failed:", error);

      const errorMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content:
          "Sorry, something went wrong while running the research.",
      };

      setMessages((previous) => [
        ...previous,
        errorMessage,
      ]);

    } finally {
      setLoading(false);
      setStatus("");
    }
  };

  return (
    <div className="flex h-screen overflow-hidden">

      <Sidebar />

      <main className="flex min-w-0 flex-1 flex-col">

        <header className="flex h-16 shrink-0 items-center border-b px-6">
          <div>
            <h2 className="font-semibold">
              Main Research
            </h2>

            <p className="text-xs text-muted-foreground">
              Your research workspace
            </p>
          </div>
        </header>

        <ChatWindow
          messages={messages}
          loading={loading}
          status={status}
        />

        <ChatInput
          value={message}
          onChange={setMessage}
          onSubmit={handleSubmit}
          loading={loading}
        />

      </main>

    </div>
  );
}

export default MainResearch;