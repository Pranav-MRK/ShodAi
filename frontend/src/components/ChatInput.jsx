import { ArrowUp } from "lucide-react";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";

function ChatInput({ value, onChange, onSubmit, loading }) {
  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();

      if (!loading) {
        onSubmit();
      }
    }
  };

  return (
    <div className="border-t p-4">
      <div className="mx-auto flex max-w-3xl items-end gap-2 rounded-xl border bg-background p-2 shadow-sm">

        <Textarea
          value={value}
          onChange={(event) => onChange(event.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask a research question..."
          disabled={loading}
          className="min-h-[50px] resize-none border-0 shadow-none focus-visible:ring-0"
        />

        <Button
          size="icon"
          onClick={onSubmit}
          disabled={loading || !value.trim()}
          className="mb-0.5"
        >
          <ArrowUp size={18} />
        </Button>

      </div>

      <p className="mt-2 text-center text-xs text-muted-foreground">
        Press Enter to send · Shift + Enter for a new line
      </p>
    </div>
  );
}

export default ChatInput;