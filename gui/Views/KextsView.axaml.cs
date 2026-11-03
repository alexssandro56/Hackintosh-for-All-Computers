// The kexts this program can put in an EFI, and where each came from.
using System.Linq;
using System.Threading.Tasks;
using Avalonia.Controls;
using Shell.Engine;

namespace Shell.Views;

public sealed class KextItem
{
    public KextItem(KextRow row)
    {
        Bundle = row.Bundle;
        Upstream = row.Upstream ?? L.T("no upstream recorded");
        Version = row.Version ?? "—";
        // "none stated" is the absence of a licence, not a permissive one, and
        // the table says so in the same words the licence file does
        Licence = row.Licence ?? L.T("unread");
        // The table is generated from what each kext binds to by device id.
        // AppleALC matches on a layout, Lilu on nothing at all - neither is
        // idle, and neither has a row, so this says what is true of both.
        Drives = row.Label ?? L.T("not matched by device id");
        Devices = row.Devices == 1 ? L.T("1 device id") : L.F("{0} device ids", row.Devices);
        HasDevices = row.Devices > 0;
    }

    public string Bundle { get; }
    public string Upstream { get; }
    public string Version { get; }
    public string Licence { get; }
    public string Drives { get; }
    public string Devices { get; }
    public bool HasDevices { get; }
}

public partial class KextsView : UserControl
{
    Task? _loaded;

    public KextsView()
    {
        InitializeComponent();
        L.Apply(this);
    }

    /// <summary>Read the list the first time this pane is looked at.</summary>
    // One read, and everybody waits for the same one. A bool guard let the
    // second caller past while the first was still awaiting: the nav's own
    // handler starts a Swap of its own, so two arrive together, and the second
    // returned to a pane that had not been filled yet. The screenshot pass
    // caught it on an empty list.
    public Task Load()
    {
        // and a read that threw is not a read: keeping the faulted task would
        // make every later look at this pane raise the same old exception
        if (_loaded is { IsFaulted: true }) _loaded = null;
        return _loaded ??= Fill();
    }

    async Task Fill()
    {
        var engine = Builder.Find(out var missing);
        if (engine is null) { Blurb.Text = missing; return; }

        var (list, complaint) = await Inventory.Kexts(engine);
        if (list is null) { Blurb.Text = complaint; return; }

        var claiming = list.Kexts.Count(k => k.Devices > 0);
        var ids = list.Kexts.Sum(k => k.Devices);
        Blurb.Text = L.F("{0} kexts travel inside this program, so a build " +
                     "never reaches the network. {1} of them claim {2} device " +
                     "ids between them, read out of the kexts themselves rather than " +
                     "from a list somebody kept.", list.Kexts.Count, claiming, ids);
        Rows.ItemsSource = list.Kexts.Select(k => new KextItem(k)).ToList();
    }
}
