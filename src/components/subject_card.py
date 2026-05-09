import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#1E293B; border-left: 8px solid #3B82F6; padding:25px; border-radius: 20px; border: 1px solid #334155; margin-bottom:20px;">
        <h3 style="margin:0; color:#F8FAFC; font-size:1.5rem;">{name}</h3>
        <p style="color:#94A3B8; margin:10px 0;">Code : <span style="background:#3B82F620; color:#3B82F6; padding:2px 8px; border-radius:5px;">{code}</span> | Section : {section}</p>
    """

    if stats:
        html += """<div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:10px;">"""

        for icon, label, value in stats:
            # Different color for each stat
            if label == "Students":
                bg, color = "#F59E0B20", "#F59E0B"   # Amber
            elif label == "Classes":
                bg, color = "#10B98120", "#10B981"   # Emerald
            else:
                bg, color = "#8B5CF620", "#8B5CF6"   # Purple

            html += f'''
                <div style="background:{bg}; border:1px solid {color}40; padding:6px 14px; border-radius:12px; font-size:0.9rem; color:{color};">
                    {icon} <b>{value}</b> {label}
                </div>'''

        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()