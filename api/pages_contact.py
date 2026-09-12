"""/contact page with direct submission and an email fallback."""
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

FORM_SCRIPT = """
<script>
(function(){
  var f=document.getElementById('project-form');
  if(!f)return;
  var note=document.getElementById('form-note');
  var button=f.querySelector('button[type="submit"]');
  var setStatus=function(message,isError){
    note.textContent=message;note.hidden=false;
    note.classList.toggle('form-note--error',!!isError);
  };
  f.addEventListener('submit',async function(e){
    e.preventDefault();
    var g=function(n){var el=f.elements[n];return el?el.value.trim():'';};
    var tests={
      name:function(v){return !!v;},
      email:function(v){return /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(v);},
      website:function(v){if(!v)return true;try{new URL(v);return true;}catch(_){return false;}}
    };
    var ok=true,firstInvalid=null;
    Object.keys(tests).forEach(function(name){
      var w=f.querySelector('[data-field="'+name+'"]');
      if(!w)return;
      var input=f.elements[name],bad=!tests[name](g(name));
      w.classList.toggle('field--error',bad);
      input.setAttribute('aria-invalid',bad?'true':'false');
      if(bad){ok=false;if(!firstInvalid)firstInvalid=input;}
    });
    if(!ok){setStatus('Please correct the highlighted fields.',true);firstInvalid.focus();return;}
    button.disabled=true;button.textContent='Sending...';note.hidden=true;
    try{
      var data=Object.fromEntries(new FormData(f).entries());
      var response=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
      var result=await response.json();
      if(!response.ok)throw new Error(result.error||'Your message could not be sent.');
      f.reset();
      f.querySelectorAll('[aria-invalid]').forEach(function(el){el.setAttribute('aria-invalid','false');});
      setStatus('Thanks. Your project details have been sent, and I will reply by email.',false);
    }catch(error){
      setStatus(error.message+' You can still use Email directly.',true);
    }finally{
      button.disabled=false;button.textContent='Send project details →';
    }
  });
})();
</script>
"""


def _field(label, name, type_="text", required=False, placeholder=""):
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    required_attr = ' required aria-required="true"' if required else ""
    ph = f' placeholder="{esc(placeholder)}"' if placeholder else ""
    validates = required or type_ in {"email", "url"}
    describedby = f' aria-describedby="f-{name}-error"' if validates else ""
    error = (f'<span class="field__err" id="f-{name}-error">'
             f'Please add a valid {esc(label.lower())}.</span>') if validates else ""
    return f"""
    <div class="field" data-field="{name}">
      <label for="f-{name}">{esc(label)}{req}</label>
      <input type="{type_}" id="f-{name}" name="{name}"{required_attr}{describedby}{ph}>
      {error}
    </div>"""


def render() -> str:
    body = f"""
<section class="section">
  <div class="container" style="max-width:720px">
    <span class="eyebrow">Hire me</span>
    <h1>Tell me what you need written.</h1>
    <p class="lede" style="margin-top:var(--sp-5)">Share the product, audience, deliverable, and
    timeline. I'll review the brief and reply with the next steps.</p>

    <form id="project-form" style="margin-top:var(--sp-8)" novalidate>
      <div class="hp-field" aria-hidden="true">
        <label for="website-check">Leave this field empty</label>
        <input id="website-check" name="website_check" tabindex="-1" autocomplete="off">
      </div>
      <div class="form-grid">
        {_field("Name", "name", required=True)}
        {_field("Email", "email", type_="email", required=True)}
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
      <p id="form-note" hidden class="muted" role="status" aria-live="polite" style="margin-top:var(--sp-4)"></p>
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
