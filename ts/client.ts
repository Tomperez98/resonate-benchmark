
import { Resonate } from "@resonatehq/sdk";
import express, { type Request, type Response } from "express";

import { v4 as uuidv4 } from "uuid";

const resonate = Resonate.remote({ url:"http://localhost:8001" });

const app = express();

app.get("/", async (req: Request, res: Response) => {
  const identifier = uuidv4();

  const h = await resonate.beginRpc(
      identifier,
      "foo",
      identifier,
      resonate.options({ target: "poll://any@foo_nodes" })
    );
  const result = await h.result()


  res.json({
    time: new Date().toISOString(),
    message: result
  });
});

app.listen(8081, () => {
  console.info(`resonate-benchmark running on http://localhost:8081`);
});
