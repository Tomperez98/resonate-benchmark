import { Resonate, type Context } from "@resonatehq/sdk";
import type { Yieldable } from "@resonatehq/sdk/dist/src/types";

const resonate = Resonate.remote({group: "foo_nodes", url:"http://localhost:8001"})

function* foo(ctx: Context, identifier: string): Generator<Yieldable, string, any> {
  return (yield* ctx.run(bar, identifier));
}

function bar(_: Context, identifier: string): string {
  return `id: ${identifier}`;
}
resonate.register( foo)

console.log("worker running...")
