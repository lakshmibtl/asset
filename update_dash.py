import sys
import re

file_path = '/home/btl/asset1/asset_app/templates/asset_app/dashboard.html'
with open(file_path, 'r') as f:
    content = f.read()

# Find the admin section
admin_start = content.find('{% else %}')
if admin_start == -1:
    print("Could not find {% else %} block")
    sys.exit(1)

new_admin_content = """{% else %}
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    .admin-layout {
        background-color: #f4f7fe;
        min-height: 100vh;
        padding: 2rem 1.5rem;
        font-family: 'Inter', sans-serif;
    }

    .admin-header { display: none; } /* Hide old header to match clean mockup */

    /* Grids */
    .crypto-top-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .crypto-mid-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .crypto-btm-grid {
        display: grid;
        grid-template-columns: 2fr 1.5fr;
        gap: 1.5rem;
    }

    @media (max-width: 1200px) {
        .crypto-top-grid { grid-template-columns: repeat(2, 1fr); }
        .crypto-mid-grid { grid-template-columns: 1fr 1fr; }
        .crypto-btm-grid { grid-template-columns: 1fr; }
    }
    @media (max-width: 768px) {
        .crypto-top-grid, .crypto-mid-grid { grid-template-columns: 1fr; }
    }

    /* Cards */
    .c-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .c-card-blue {
        background: #4361ee;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 8px 25px rgba(67, 97, 238, 0.4);
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: relative;
        overflow: hidden;
    }
    .c-card-blue::after {
        content: '';
        position: absolute;
        top: -20px;
        right: -20px;
        width: 120px;
        height: 120px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
    }

    /* Top Card Details */
    .c-title {
        font-size: 0.85rem;
        font-weight: 500;
        color: #64748b;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.75rem;
    }
    .c-card-blue .c-title { color: rgba(255,255,255,0.8); }
    .c-icon {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
    }
    .ci-gray { background: #f1f5f9; color: #475569; }
    .ci-blue { background: rgba(255,255,255,0.2); color: white; }
    .c-val {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.25rem;
    }
    .c-card-blue .c-val { color: white; }
    
    .c-pill {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 600;
    }
    .cp-green { background: #dcfce7; color: #166534; }
    .c-card-blue .cp-green { background: rgba(255,255,255,0.2); color: white; }

    /* Panels */
    .c-panel {
        background: #ffffff;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .cp-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .cp-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1e293b;
    }
    .btn-dark {
        background: #0f172a; color: white; border: none; padding: 0.5rem 1.25rem; border-radius: 20px; font-weight: 600; font-size: 0.8rem; text-decoration: none;
    }
    .btn-blue {
        background: #4361ee; color: white; border: none; padding: 0.5rem 1.25rem; border-radius: 20px; font-weight: 600; font-size: 0.8rem; text-decoration: none;
    }

    /* Small Status Cards */
    .c-small-card {
        flex: 1; border-radius: 20px; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between;
    }
    .c-small-card.dark { background: #0f172a; color: white; }
    .c-small-card.blue { background: #4361ee; color: white; }
    .cs-title { font-size: 0.8rem; opacity: 0.8; margin-bottom: 1rem; }
    .cs-val { font-size: 1.5rem; font-weight: 700; }
    .cs-sub { font-size: 0.75rem; margin-top: 0.5rem; opacity: 0.8; }

    /* List */
    .c-list { list-style: none; padding: 0; margin: 0; }
    .c-list-item {
        display: flex; align-items: center; justify-content: space-between; padding: 0.75rem 0; border-bottom: 1px solid #f1f5f9;
    }
    .c-list-item:last-child { border-bottom: none; }
    .cl-icon { width: 36px; height: 36px; border-radius: 10px; background: #f1f5f9; display: flex; align-items: center; justify-content: center; color: #475569; margin-right: 1rem; }
    .cl-name { font-size: 0.85rem; font-weight: 600; color: #1e293b; margin-bottom: 0.1rem; }
    .cl-date { font-size: 0.75rem; color: #94a3b8; }
    .cl-status { font-size: 0.8rem; font-weight: 600; text-align: right; }
    .cls-pending { color: #f59e0b; }
    .cls-approved { color: #10b981; }
    .cls-rejected { color: #ef4444; }
</style>

<div class="admin-layout">
    <!-- Top Row -->
    <div class="crypto-top-grid">
        <div class="c-card">
            <div>
                <div class="c-title"><div class="c-icon ci-gray"><i class="bi bi-box-seam"></i></div> Total Assets</div>
                <div class="c-val">{{ total_assets }}</div>
            </div>
            <div><span class="c-pill cp-green"><i class="bi bi-arrow-up-short"></i> Active</span></div>
        </div>
        <div class="c-card">
            <div>
                <div class="c-title"><div class="c-icon ci-gray"><i class="bi bi-people"></i></div> Team Members</div>
                <div class="c-val">{{ total_team_members }}</div>
            </div>
            <div><span class="c-pill cp-green"><i class="bi bi-arrow-up-short"></i> Active</span></div>
        </div>
        <div class="c-card-blue">
            <div>
                <div class="c-title"><div class="c-icon ci-blue"><i class="bi bi-hourglass-split"></i></div> Pending</div>
                <div class="c-val">{{ pending }}</div>
            </div>
            <div><span class="c-pill cp-green"><i class="bi bi-check2"></i> Requires Action</span></div>
        </div>
        <div class="c-card">
            <div>
                <div class="c-title"><div class="c-icon ci-gray"><i class="bi bi-check-circle"></i></div> Approved</div>
                <div class="c-val">{{ approved }}</div>
            </div>
            <div><span class="c-pill cp-green"><i class="bi bi-arrow-up-short"></i> Resolved</span></div>
        </div>
    </div>

    <!-- Middle Row -->
    <div class="crypto-mid-grid">
        <div class="c-panel">
            <div class="cp-header">
                <span class="cp-title">Requests Overview</span>
                <i class="bi bi-three-dots text-muted"></i>
            </div>
            <div class="mb-2">
                <span style="font-size:2rem; font-weight:700; color:#1e293b;">{{ total_reqs }}</span>
                <span style="font-size:0.8rem; color:#10b981; margin-left:8px;"><i class="bi bi-arrow-up-short"></i> Total requests</span>
            </div>
            <div style="flex-grow:1; position:relative; min-height:150px;">
                <canvas id="cLineChart"></canvas>
            </div>
            <div class="d-flex gap-2 mt-3">
                <a href="{% url 'procurement_list' %}" class="btn-dark"><i class="bi bi-arrow-down-short"></i> View All</a>
                <a href="{% url 'create_procurement' %}" class="btn-blue"><i class="bi bi-plus-lg"></i> New Request</a>
            </div>
        </div>

        <div class="c-panel">
            <div class="cp-header">
                <span class="cp-title">Asset Categories</span>
                <i class="bi bi-three-dots text-muted"></i>
            </div>
            <div style="flex-grow:1; position:relative; min-height:200px; display:flex; align-items:center; justify-content:center;">
                <canvas id="cDonutChart"></canvas>
            </div>
        </div>

        <div style="display:flex; flex-direction:column; gap:1.5rem;">
            <div class="c-panel" style="flex:auto; padding:1rem 1.5rem; display:flex; flex-direction:row; justify-content:space-between; align-items:center;">
                <span class="cp-title mb-0">Asset Status</span>
                <i class="bi bi-chevron-right text-muted"></i>
            </div>
            <div style="display:flex; gap:1rem; height:100%;">
                <div class="c-small-card dark">
                    <div class="cs-title"><i class="bi bi-laptop"></i> In Use</div>
                    <div><div class="cs-val">{{ assets_in_use }}</div><div class="cs-sub">Assigned</div></div>
                </div>
                <div class="c-small-card blue">
                    <div class="cs-title"><i class="bi bi-check2-circle"></i> Available</div>
                    <div><div class="cs-val">{{ available_assets }}</div><div class="cs-sub">Ready</div></div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bottom Row -->
    <div class="crypto-btm-grid">
        <div class="c-panel">
            <div class="cp-header">
                <span class="cp-title">Requests Overviews</span>
                <div class="d-flex gap-2">
                    <span class="badge bg-light text-dark border rounded-pill">Pending</span>
                    <span class="badge bg-dark text-white rounded-pill">Approved</span>
                </div>
            </div>
            <div style="flex-grow:1; position:relative; min-height:250px;">
                <canvas id="cBarChart"></canvas>
            </div>
        </div>

        <div class="c-panel">
            <div class="cp-header">
                <span class="cp-title">Recent Requests</span>
                <a href="{% url 'procurement_list' %}" class="btn-dark" style="padding:0.25rem 1rem;">View All</a>
            </div>
            <ul class="c-list">
                {% for r in requests_list|slice:":5" %}
                <li class="c-list-item">
                    <div style="display:flex; align-items:center;">
                        <div class="cl-icon"><i class="bi bi-file-earmark-text"></i></div>
                        <div>
                            <div class="cl-name">{{ r.requested_by.username|title }} - {{ r.asset_type }}</div>
                            <div class="cl-date">{{ r.request_date|date:"d M Y, h:i A" }}</div>
                        </div>
                    </div>
                    <div>
                        {% if r.status == 'Approved' %}<div class="cl-status cls-approved">+ Approved</div>
                        {% elif r.status == 'Rejected' %}<div class="cl-status cls-rejected">- Rejected</div>
                        {% else %}<div class="cl-status cls-pending">Pending</div>{% endif %}
                    </div>
                </li>
                {% empty %}
                <li class="text-center text-muted py-4">No recent requests</li>
                {% endfor %}
            </ul>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    Chart.defaults.font.family = "'Inter', sans-serif";
    Chart.defaults.color = '#64748b';

    const lCtx = document.getElementById('cLineChart');
    if (lCtx) {
        new Chart(lCtx, {
            type: 'line',
            data: {
                labels: {{ line_chart_labels|safe|default:"['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']" }},
                datasets: [{
                    label: 'Requests',
                    data: {{ line_chart_total|safe|default:"[10, 20, 15, 30, 25, 40]" }},
                    borderColor: '#0f172a', backgroundColor: '#0f172a', tension: 0.4, borderWidth: 3, pointRadius: 0, pointHoverRadius: 6
                }]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { display: false }, y: { display: false, min: 0 } } }
        });
    }

    const dCtx = document.getElementById('cDonutChart');
    if (dCtx) {
        new Chart(dCtx, {
            type: 'doughnut',
            data: {
                labels: {{ asset_types_json|safe|default:"['Laptops', 'Desktops', 'Mobiles']" }},
                datasets: [{
                    data: {{ asset_type_counts_json|safe|default:"[40, 30, 30]" }},
                    backgroundColor: ['#0f172a', '#4361ee', '#e2e8f0', '#f1f5f9'], borderWidth: 0, hoverOffset: 5
                }]
            },
            options: { responsive: true, maintainAspectRatio: false, cutout: '75%', plugins: { legend: { position: 'bottom', labels: { usePointStyle: true, padding: 20, font: { size: 12, weight: '500' } } } } }
        });
    }

    const bCtx = document.getElementById('cBarChart');
    if (bCtx) {
        new Chart(bCtx, {
            type: 'bar',
            data: {
                labels: {{ line_chart_labels|safe|default:"['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']" }},
                datasets: [
                    { label: 'Approved', data: {{ line_chart_approved|safe|default:"[5, 12, 10, 20, 18, 30]" }}, backgroundColor: '#0f172a', borderRadius: 6, barThickness: 12 },
                    { label: 'Pending', data: {{ line_chart_pending|safe|default:"[5, 8, 5, 10, 7, 10]" }}, backgroundColor: '#4361ee', borderRadius: 6, barThickness: 12 }
                ]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { grid: { borderDash: [4, 4], color: '#f1f5f9' }, beginAtZero: true } } }
        });
    }
});
</script>
{% endif %}
{% endblock %}"""

new_content = content[:admin_start] + new_admin_content

with open(file_path, 'w') as f:
    f.write(new_content)
