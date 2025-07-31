//frontend/src/app/api/test-backend/route.ts
export async function GET() {
    try {
        const res = await fetch("http://localhost:8000/");
        const data = await res.json();
        return new Response(JSON.stringify(data), {
            headers: {
                "Content-Type": "application/json",
            },
            status: 200,
        });
    } catch (error) {
        return new Response(JSON.stringify({ error: "Failed to fetch data" }), {
            headers: {
                "Content-Type": "application/json",
            },
            status: 500,
        });
    }
}

//http://127.0.0.1:8000/