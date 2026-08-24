"use client";

import { useState } from "react";
import TabNav from "@/components/TabNav";
import { TABS, TabId } from "@/lib/types";
import Overview from "@/components/tabs/Overview";
import BankAccounts from "@/components/tabs/BankAccounts";
import Turkcell from "@/components/tabs/Turkcell";
import TurkTelekom from "@/components/tabs/TurkTelekom";
import Subscriptions from "@/components/tabs/Subscriptions";
import Vault from "@/components/tabs/Vault";

const TAB_CONTENT: Record<TabId, () => React.ReactElement> = {
  overview: Overview,
  bank: BankAccounts,
  turkcell: Turkcell,
  turktelekom: TurkTelekom,
  subscriptions: Subscriptions,
  vault: Vault,
};

interface DashboardProps {
  onLock: () => void;
}

export default function Dashboard({ onLock }: DashboardProps) {
  const [activeTab, setActiveTab] = useState<TabId>("overview");
  const ActiveContent = TAB_CONTENT[activeTab];
  const activeMeta = TABS.find((tab) => tab.id === activeTab)!;

  return (
    <div className="min-h-screen bg-[var(--background)]">
      <header className="flex items-center justify-between border-b border-[var(--border)] px-4 py-3 sm:px-6">
        <div className="flex items-center gap-2">
          <span className="text-lg">🔐</span>
          <span className="text-sm font-semibold">Finans &amp; Hesap Paneli</span>
        </div>
        <button
          onClick={onLock}
          className="rounded-lg border border-[var(--border)] px-3 py-1.5 text-xs text-[var(--muted)] transition hover:text-[var(--foreground)]"
        >
          Kilitle
        </button>
      </header>

      <TabNav activeTab={activeTab} onChange={setActiveTab} />

      <main className="mx-auto max-w-5xl px-4 py-6 sm:px-6">
        <div className="mb-4">
          <h1 className="text-lg font-semibold text-[var(--foreground)]">
            {activeMeta.label}
          </h1>
          <p className="text-sm text-[var(--muted)]">{activeMeta.description}</p>
        </div>
        <ActiveContent />
      </main>
    </div>
  );
}
