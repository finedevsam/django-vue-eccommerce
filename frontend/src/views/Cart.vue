<template>
  <div class="page-cart">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">Cart</h1>
          </div>
          <div class="column is-12 box">
              <table class="table is-fullwidth" v-if="cartTotalLength">
                  <head>
                      <tr>
                          <th>Product</th>
                          <th>price</th>
                          <th>Quantity</th>
                          <th>Total</th>
                          <th></th>
                      </tr>
                  </head>
                  <tbody>
                      <CartItem v-for="item in cart.items" v-bind:key="item.product.id" v-bind:initialItem="item" />
                  </tbody>
              </table>
              <p v-else>You don't have any product in your Cart........</p>
          </div>
          <div class="column is-12 box">
              <h2 class="subtitle">Summary</h2>
              <strong>₦ {{cartTotalPrice.toFixed(2)}}</strong>, {{cartTotalLength}} Items
              <hr>
              <router-link to="/cart/checkout" class="button is-dark">Proceed to checkout</router-link>
          </div>
      </div>
  </div>
</template>

<script>
// import axios from 'axios'
import CartItem from '@/components/CartItem'
export default {
    name: 'Cart',
    components:{
        CartItem
    },
    data() {
        return {
            
            cart: {
                items: [],
                
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    computed: {
        cartTotalLength(){
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        }
    }
}
</script>

<style>

</style>