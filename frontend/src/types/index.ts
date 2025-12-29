export interface User {
    id: string
    email: string
    tenant_id: string
    first_name: string
    last_name: string
    date_of_birth: string
    phone: string
    role: string
    is_active: boolean
    created_at?: string
}