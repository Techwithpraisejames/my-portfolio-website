"""/contact page. Mailto-based project inquiry form."""
from components import breadcrumbs, esc
from content import CONTACT_EMAIL, PROJECT_TYPES
from seo import PageMeta, breadcrumb_list
from shell import render_page

META = PageMeta(
    title="Hire me | Contact Praise James",
    description=(
        "Tell Praise James what you're building and what you need help with: technical articles, "
        "developer tutorials, product-led content, or thought leadership."
    ),
    path="/contact",
)

_OPTIONS = "".join(f'<option value="{esc(t)}">{esc(t)}</option>' for t in PROJECT_TYPES)

FORM_SCRIPT = f"""
<script>
(function(){{
  var f=document.getElementById('project-form');
  if(!f)return;
  f.addEventListener('submit',function(e){{
    e.preventDefault();
    var g=function(n){{var el=f.elements[n];return el?el.value.trim():'';}};
    var name=g('name'),email=g('email');
    var ok=true;
    [['name',name],['email',email]].forEach(function(p){{
      var w=f.querySelector('[data-field="'+p[0]+'"]');
      if(!w)return;
      var bad=!p[1]||(p[0]==='email'&&!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(p[1]));
      w.classList.toggle('field--error',bad); if(bad)ok=false;
    }});
    if(!ok)return;
    var lines=[
      'Name: '+name,'Work email: '+email,
      'Company: '+g('company'),'Website: '+g('website'),
      'What they need: '+g('need'),'Timeline: '+g('timeline'),
      'Budget range: '+g('budget'),'',
      'Project:',g('details')
    ];
    var href='mailto:{CONTACT_EMAIL}'
      +'?subject='+encodeURIComponent('Project inquiry: '+(g('need')||'Technical content')+' from '+name)
      +'&body='+encodeURIComponent(lines.join('\\n'));
    window.location.href=href;
    var note=document.getElementById('form-note');
    if(note)note.hidden=false;
  }});
}})();
</script>
"""


def _field(label, name, type_="text", required=False, placeholder=""):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    aria = ' aria-required="true"' if required else ""
    ph = f' placeholder="{esc(placeholder)}"' if placeholder else ""
    return f"""
    <div class="field" data-field="{name}">
      <label for="f-{name}">{esc(label)}{req}</label>
      <input type="{type_}" id="f-{name}" name="{name}"{aria}{ph}>
      <span class="field__err">Please add a valid {esc(label.lower())}.</span>
    </div>"""


def render() -> str:
    body = f"""
<section class="section">
  <div class="container" style="max-width:720px">
    <span class="eyebrow">Hire me</span>
    <h1>Have a technical story that needs telling?</h1>
    <p class="lede" style="margin-top:var(--sp-5)">Tell me what you're building, what you need help
    with, and where you're trying to take the content.</p>

    <form id="project-form" style="margin-top:var(--sp-8)" novalidate>
      <div class="form-grid">
        {_field("Name", "name", required=True)}
        {_field("Work email", "email", type_="email", required=True)}
        {_field("Company", "company")}
        {_field("Website", "website", type_="url", placeholder="https://")}
      </div>
      <div class="field">
        <label for="f-need">What do you need?</label>
        <select id="f-need" name="need">{_OPTIONS}</select>
      </div>
      <div class="field">
        <label for="f-details">Tell me about the project</label>
        <textarea id="f-details" name="details"></textarea>
      </div>
      <div class="form-grid">
        {_field("Timeline", "timeline", placeholder="e.g. within a month")}
        {_field("Budget range (optional)", "budget")}
      </div>
      <div class="btn-row" style="margin-top:var(--sp-4)">
        <button type="submit" class="btn btn--accent">Send project details &rarr;</button>
        <a class="btn btn--ghost" href="mailto:{CONTACT_EMAIL}">Email directly &rarr;</a>
      </div>
      <p id="form-note" hidden class="muted" style="margin-top:var(--sp-4)">Your email client should
      open with the details filled in. If it didn't, write to
      <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>
      <noscript>
        <p class="muted" style="margin-top:var(--sp-4)">Email me directly at
        <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> with your name, company, what you need,
        and a note about the project.</p>
      </noscript>
    </form>
  </div>
</section>
{FORM_SCRIPT}
"""
    trail = [("Home", "/"), ("Hire me", "/contact")]
    return render_page(META, body, path="/contact", breadcrumbs_html=breadcrumbs(trail),
                       jsonld_blocks=[breadcrumb_list(trail)])
