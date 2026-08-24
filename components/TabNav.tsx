"use client";

import { TABS, TabId } from "@/lib/types";

interface TabNavProps {
  activeTab: TabId;
  onChange: (tab: TabId) => void;
}

export default function TabNav({ activeTab, onChange }: TabNavProps) {
  return (
    <nav className="flex gap-1 overflow-x-auto border-b border-[var(--border)] px-4 sm:px-6">
      {TABS.map((tab) => {
        const isActive = tab.id === activeTab;
        return (
          <button
            key={tab.id}
            onClick={() => onChange(tab.id)}
            className={`whitespace-nowrap border-b-2 px-3 py-3 text-sm font-medium transition ${
              isActive
                ? "border-[var(--accent)] text-[var(--foreground)]"
                : "border-transparent text-[var(--muted)] hover:text-[var(--foreground)]"
            }`}
          >
            {tab.label}
          </button>
        );
      })}
    </nav>
  );
}
