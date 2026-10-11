import { FileText, MessageSquare, Plus, Search } from "lucide-react";

function Sidebar() {
  return (
    <aside className="flex h-screen w-72 flex-col border-r bg-background">

      {/* Header */}
      <div className="flex h-16 items-center justify-between border-b px-5">
        <h1 className="text-xl font-semibold tracking-tight">
          Shod
        </h1>

        <button className="rounded-md p-2 hover:bg-muted">
          <Plus size={18} />
        </button>
      </div>

      {/* Search */}
      <div className="p-4">
        <div className="flex items-center gap-2 rounded-md border px-3 py-2">
          <Search size={16} className="text-muted-foreground" />

          <input
            placeholder="Search research..."
            className="w-full bg-transparent text-sm outline-none"
          />
        </div>
      </div>

      {/* Main chat */}
      <div className="px-3">
        <p className="mb-2 px-2 text-xs font-medium uppercase text-muted-foreground">
          Research
        </p>

        <button className="flex w-full items-center gap-3 rounded-md bg-muted px-3 py-2 text-sm">
          <MessageSquare size={17} />
          Main Research
        </button>
      </div>

      {/* Papers */}
      <div className="mt-6 flex-1 px-3">

        <p className="mb-2 px-2 text-xs font-medium uppercase text-muted-foreground">
          Papers
        </p>

        <div className="space-y-1">

          <button className="flex w-full items-center gap-3 rounded-md px-3 py-2 text-left text-sm hover:bg-muted">
            <FileText size={16} />
            Paper A
          </button>

          <button className="flex w-full items-center gap-3 rounded-md px-3 py-2 text-left text-sm hover:bg-muted">
            <FileText size={16} />
            Paper B
          </button>

        </div>
      </div>

      {/* Footer */}
      <div className="border-t p-4">
        <p className="text-xs text-muted-foreground">
          Shod Research Agent
        </p>
      </div>

    </aside>
  );
}

export default Sidebar;