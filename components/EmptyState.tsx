interface EmptyStateProps {
  icon: string;
  title: string;
  description: string;
  note?: string;
}

export default function EmptyState({
  icon,
  title,
  description,
  note,
}: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center rounded-2xl border border-dashed border-[var(--border)] bg-[var(--surface)] px-6 py-16 text-center">
      <div className="mb-4 text-4xl">{icon}</div>
      <h2 className="text-base font-semibold text-[var(--foreground)]">
        {title}
      </h2>
      <p className="mt-2 max-w-md text-sm text-[var(--muted)]">
        {description}
      </p>
      {note && (
        <p className="mt-4 max-w-md rounded-lg border border-[var(--border)] bg-[var(--surface-2)] px-3 py-2 text-xs text-[var(--muted)]">
          {note}
        </p>
      )}
    </div>
  );
}
