# Developer Handoff Guide

**Structure**: backend/, frontend/, mobile/, docs/

**Setup**:
1. `pip install -r requirements.txt`
2. `npm install`
3. `expo install` (mobile)
4. `docker-compose up --build`

**Key Endpoints**:
- `POST /api/token/`
- `/api/checkbook/:property_id/`
- `/api/client/kpi-settings/`
- `/api/client/capex/`
- `/api/vendor/loyalty/`
- `/api/tenant/ticket/`

**Next Steps**:
- Add CI/CD
- Configure email/SMS
- Implement SMS alerts
