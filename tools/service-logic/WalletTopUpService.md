## Business logic

Card only (`CREDIT_CARD`) with a Stripe token. The amount is converted to cents exactly; a declined or uncaptured charge fails with 409 and the wallet is not credited. A successful charge records the Stripe charge id and credits the wallet.
